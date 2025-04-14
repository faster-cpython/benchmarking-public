# Results vs. 3.12.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: windows-amd64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.075x faster
- HPT reliability: 99.18%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| docutils       | 1.66 sec                                                    | 1.72 sec: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 407 ms: 1.90x faster                                                        |
| async_tree_io              | 731 ms                                                      | 420 ms: 1.74x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 174 ms: 1.64x faster                                                        |
| async_tree_none            | 291 ms                                                      | 186 ms: 1.56x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 218 ms: 1.56x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 341 ms: 1.47x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 338 ms: 1.45x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.62x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 47.0 ms: 1.21x faster                                                       |
| nbody          | 71.9 ms                                                     | 60.9 ms: 1.18x faster                                                       |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.48 ms: 1.09x faster                                                       |
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                        |
| regex_compile  | 87.5 ms                                                     | 83.4 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.37 sec                                                    | 1.25 sec: 1.10x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 122 us: 1.09x faster                                                        |
| xml_etree_generate   | 55.8 ms                                                     | 52.0 ms: 1.07x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 87.4 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.1 ms: 1.05x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.80 us: 1.02x slower                                                       |
| json_loads           | 13.9 us                                                     | 15.0 us: 1.08x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.80 us: 1.08x slower                                                       |
| pickle_dict          | 18.4 us                                                     | 20.3 us: 1.10x slower                                                       |
| pickle_pure_python   | 195 us                                                      | 219 us: 1.12x slower                                                        |
| pickle               | 7.43 us                                                     | 8.56 us: 1.15x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.33 us: 1.18x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.79 ms: 1.19x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.4 ms: 1.25x slower                                                       |
| python_startup         | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.66 ms: 1.25x faster                                                       |
| django_template | 22.9 ms                                                     | 25.2 ms: 1.10x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.7 ms: 2.46x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 407 ms: 1.90x faster                                                        |
| async_tree_io              | 731 ms                                                      | 420 ms: 1.74x faster                                                        |
| mdp                        | 1.37 sec                                                    | 792 ms: 1.73x faster                                                        |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 174 ms: 1.64x faster                                                        |
| async_tree_none            | 291 ms                                                      | 186 ms: 1.56x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 218 ms: 1.56x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 341 ms: 1.47x faster                                                        |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.44 sec: 1.45x faster                                                      |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 338 ms: 1.45x faster                                                        |
| deepcopy                   | 238 us                                                      | 188 us: 1.27x faster                                                        |
| mako                       | 7.09 ms                                                     | 5.66 ms: 1.25x faster                                                       |
| generators                 | 22.5 ms                                                     | 18.3 ms: 1.23x faster                                                       |
| float                      | 56.8 ms                                                     | 47.0 ms: 1.21x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.13 ms: 1.20x faster                                                       |
| scimark_fft                | 184 ms                                                      | 154 ms: 1.20x faster                                                        |
| nbody                      | 71.9 ms                                                     | 60.9 ms: 1.18x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.2 us: 1.16x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.14x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 20.9 us: 1.13x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 59.4 ms: 1.13x faster                                                       |
| pyflate                    | 295 ms                                                      | 265 ms: 1.11x faster                                                        |
| tomli_loads                | 1.37 sec                                                    | 1.25 sec: 1.10x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 122 us: 1.09x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.48 ms: 1.09x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 52.0 ms: 1.07x faster                                                       |
| raytrace                   | 192 ms                                                      | 180 ms: 1.07x faster                                                        |
| go                         | 91.6 ms                                                     | 85.7 ms: 1.07x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 87.4 ms: 1.06x faster                                                       |
| chaos                      | 43.3 ms                                                     | 40.8 ms: 1.06x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.4 ms: 1.06x faster                                                       |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.99 us: 1.05x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 83.4 ms: 1.05x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.1 ms: 1.05x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 58.1 ns: 1.04x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 42.9 ms: 1.03x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 47.2 ms: 1.03x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 1.03 sec: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| nqueens                    | 62.8 ms                                                     | 62.1 ms: 1.01x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 92.2 ms: 1.01x slower                                                       |
| richards_super             | 32.1 ms                                                     | 32.4 ms: 1.01x slower                                                       |
| richards                   | 28.4 ms                                                     | 28.7 ms: 1.01x slower                                                       |
| async_generators           | 239 ms                                                      | 244 ms: 1.02x slower                                                        |
| unpickle_list              | 2.75 us                                                     | 2.80 us: 1.02x slower                                                       |
| json                       | 3.05 ms                                                     | 3.10 ms: 1.02x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 60.5 ms: 1.03x slower                                                       |
| 2to3                       | 218 ms                                                      | 224 ms: 1.03x slower                                                        |
| meteor_contest             | 74.6 ms                                                     | 76.7 ms: 1.03x slower                                                       |
| unpack_sequence            | 37.5 ns                                                     | 38.5 ns: 1.03x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.48 us: 1.03x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 81.4 ms: 1.03x slower                                                       |
| fannkuch                   | 247 ms                                                      | 255 ms: 1.03x slower                                                        |
| logging_format             | 6.72 us                                                     | 6.95 us: 1.03x slower                                                       |
| docutils                   | 1.66 sec                                                    | 1.72 sec: 1.04x slower                                                      |
| sympy_str                  | 175 ms                                                      | 182 ms: 1.04x slower                                                        |
| sympy_integrate            | 13.0 ms                                                     | 13.5 ms: 1.04x slower                                                       |
| pycparser                  | 699 ms                                                      | 738 ms: 1.06x slower                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 46.2 ms: 1.06x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 517 ms: 1.06x slower                                                        |
| json_loads                 | 13.9 us                                                     | 15.0 us: 1.08x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.80 us: 1.08x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.35 ms: 1.09x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.2 ms: 1.10x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 20.3 us: 1.10x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.55 ms: 1.10x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 219 us: 1.12x slower                                                        |
| sympy_expand               | 284 ms                                                      | 319 ms: 1.12x slower                                                        |
| pickle                     | 7.43 us                                                     | 8.56 us: 1.15x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.73 ms: 1.15x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 112 us: 1.18x slower                                                        |
| pickle_list                | 2.83 us                                                     | 3.33 us: 1.18x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.79 ms: 1.19x slower                                                       |
| coverage                   | 40.8 ms                                                     | 49.4 ms: 1.21x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.4 ms: 1.25x slower                                                       |
| bench_mp_pool              | 69.2 ms                                                     | 89.0 ms: 1.29x slower                                                       |
| python_startup             | 19.5 ms                                                     | 25.7 ms: 1.32x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 2.05 ms: 1.35x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 1.25 ms: 1.67x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (4): pprint_safe_repr, regex_v8, xml_etree_process, bench_thread_pool
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-pythonperf1-amd64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.075x faster

# HPT report

- Reliability score: 99.18% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown