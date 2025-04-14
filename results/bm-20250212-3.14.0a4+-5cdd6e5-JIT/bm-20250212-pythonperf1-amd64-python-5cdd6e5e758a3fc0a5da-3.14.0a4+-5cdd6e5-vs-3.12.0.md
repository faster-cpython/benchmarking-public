# Results vs. 3.12.0

- fork: python
- ref: 5cdd6e5e758a3fc0a5da
- machine: windows-amd64
- commit hash: 5cdd6e5
- commit date: 2025-02-12
- overall geometric mean: 1.057x faster
- HPT reliability: 95.38%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 221 ms: 1.01x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.76 sec: 1.06x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 420 ms: 1.84x faster                                                        |
| async_tree_io              | 731 ms                                                      | 417 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 176 ms: 1.62x faster                                                        |
| async_tree_none            | 291 ms                                                      | 187 ms: 1.56x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.52x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 341 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 344 ms: 1.42x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.60x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 60.4 ms: 1.19x faster                                                       |
| float          | 56.8 ms                                                     | 48.4 ms: 1.17x faster                                                       |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.43 ms: 1.13x faster                                                       |
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 80.8 ms: 1.08x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 112 us: 1.18x faster                                                        |
| tomli_loads          | 1.37 sec                                                    | 1.20 sec: 1.14x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 50.3 ms: 1.11x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 60.8 ms: 1.07x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 89.9 ms: 1.03x faster                                                       |
| pickle_pure_python   | 195 us                                                      | 213 us: 1.09x slower                                                        |
| json_loads           | 13.9 us                                                     | 16.0 us: 1.15x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.76 ms: 1.19x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.1 ms: 1.29x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.33 ms: 1.33x faster                                                       |
| django_template | 22.9 ms                                                     | 25.8 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 29.5 ms: 2.73x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 420 ms: 1.84x faster                                                        |
| async_tree_io              | 731 ms                                                      | 417 ms: 1.76x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 176 ms: 1.62x faster                                                        |
| async_tree_none            | 291 ms                                                      | 187 ms: 1.56x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.52x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 341 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 344 ms: 1.42x faster                                                        |
| mako                       | 7.09 ms                                                     | 5.33 ms: 1.33x faster                                                       |
| deepcopy                   | 238 us                                                      | 188 us: 1.27x faster                                                        |
| scimark_fft                | 184 ms                                                      | 147 ms: 1.26x faster                                                        |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.05 ms: 1.25x faster                                                       |
| comprehensions             | 14.1 us                                                     | 11.6 us: 1.21x faster                                                       |
| nbody                      | 71.9 ms                                                     | 60.4 ms: 1.19x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 112 us: 1.18x faster                                                        |
| float                      | 56.8 ms                                                     | 48.4 ms: 1.17x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.54 us: 1.15x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.20 sec: 1.14x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 38.8 ms: 1.14x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.43 ms: 1.13x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 21.1 us: 1.12x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 50.3 ms: 1.11x faster                                                       |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                        |
| generators                 | 22.5 ms                                                     | 20.7 ms: 1.09x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 80.8 ms: 1.08x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 62.0 ms: 1.08x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.8 ms: 1.07x faster                                                       |
| fannkuch                   | 247 ms                                                      | 232 ms: 1.06x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.98 us: 1.06x faster                                                       |
| go                         | 91.6 ms                                                     | 87.1 ms: 1.05x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 996 ms: 1.05x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 46.3 ms: 1.05x faster                                                       |
| pyflate                    | 295 ms                                                      | 282 ms: 1.05x faster                                                        |
| xml_etree_process          | 37.7 ms                                                     | 36.2 ms: 1.04x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 89.9 ms: 1.03x faster                                                       |
| chaos                      | 43.3 ms                                                     | 42.1 ms: 1.03x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 89.7 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 14.4 ms: 1.01x slower                                                       |
| nqueens                    | 62.8 ms                                                     | 63.5 ms: 1.01x slower                                                       |
| pycparser                  | 699 ms                                                      | 707 ms: 1.01x slower                                                        |
| 2to3                       | 218 ms                                                      | 221 ms: 1.01x slower                                                        |
| meteor_contest             | 74.6 ms                                                     | 76.0 ms: 1.02x slower                                                       |
| async_generators           | 239 ms                                                      | 246 ms: 1.03x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                       |
| json                       | 3.05 ms                                                     | 3.17 ms: 1.04x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 45.6 ms: 1.04x slower                                                       |
| logging_format             | 6.72 us                                                     | 7.01 us: 1.04x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.32 ms: 1.05x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.58 us: 1.05x slower                                                       |
| sqlglot_parse              | 804 us                                                      | 844 us: 1.05x slower                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 1.08 ms: 1.05x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.76 sec: 1.06x slower                                                      |
| sympy_expand               | 284 ms                                                      | 301 ms: 1.06x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.8 ms: 1.07x slower                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 37.1 ms: 1.07x slower                                                       |
| raytrace                   | 192 ms                                                      | 208 ms: 1.08x slower                                                        |
| sqlglot_normalize          | 187 ms                                                      | 203 ms: 1.09x slower                                                        |
| pickle_pure_python         | 195 us                                                      | 213 us: 1.09x slower                                                        |
| logging_silent             | 60.5 ns                                                     | 65.8 ns: 1.09x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 64.2 ms: 1.09x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.58 ms: 1.12x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.42 ms: 1.12x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.8 ms: 1.12x slower                                                       |
| richards_super             | 32.1 ms                                                     | 36.2 ms: 1.13x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 88.9 ms: 1.13x slower                                                       |
| richards                   | 28.4 ms                                                     | 32.1 ms: 1.13x slower                                                       |
| json_loads                 | 13.9 us                                                     | 16.0 us: 1.15x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                        |
| json_dumps                 | 5.70 ms                                                     | 6.76 ms: 1.19x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                       |
| mdp                        | 1.37 sec                                                    | 1.67 sec: 1.22x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 84.3 ms: 1.22x slower                                                       |
| coverage                   | 40.8 ms                                                     | 50.0 ms: 1.23x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.1 ms: 1.29x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.99 ms: 1.31x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.22 ms: 1.63x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (3): pprint_safe_repr, sympy_str, bench_thread_pool
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20250212-3.14.0a4+-5cdd6e5-JIT/bm-20250212-pythonperf1-amd64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.057x faster

# HPT report

- Reliability score: 95.38% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown