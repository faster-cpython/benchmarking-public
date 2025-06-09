# Results vs. 3.12.0

- fork: python
- ref: b150b6aca7b17efe1bb1
- machine: windows-amd64
- commit hash: b150b6a
- commit date: 2025-06-09
- overall geometric mean: 1.072x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.62 sec: 1.03x faster                                                     |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 389 ms: 1.98x faster                                                       |
| async_tree_io              | 731 ms                                                      | 395 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                       |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.72x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 341 ms: 1.47x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.69x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.5 ms: 1.30x faster                                                      |
| nbody          | 71.9 ms                                                     | 62.7 ms: 1.15x faster                                                      |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.8 ms: 1.11x faster                                                      |
| regex_dna      | 126 ms                                                      | 119 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.53 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 87.9 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 63.8 ms: 1.02x faster                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.35 sec: 1.01x faster                                                     |
| unpickle_pure_python | 133 us                                                      | 132 us: 1.01x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 39.1 ms: 1.04x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 214 us: 1.10x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.29 ms: 1.10x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| python_startup         | 19.5 ms                                                     | 25.6 ms: 1.32x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.25x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.61 ms: 1.07x faster                                                      |
| django_template | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 31.8 ms: 2.53x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 389 ms: 1.98x faster                                                       |
| async_tree_io              | 731 ms                                                      | 395 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 210 ms: 1.75x faster                                                       |
| async_tree_none            | 291 ms                                                      | 170 ms: 1.72x faster                                                       |
| mdp                        | 1.37 sec                                                    | 808 ms: 1.70x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 169 ms: 1.69x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 328 ms: 1.49x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 341 ms: 1.47x faster                                                       |
| deepcopy                   | 238 us                                                      | 172 us: 1.39x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.32x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 17.9 us: 1.32x faster                                                      |
| float                      | 56.8 ms                                                     | 43.5 ms: 1.30x faster                                                      |
| go                         | 91.6 ms                                                     | 75.0 ms: 1.22x faster                                                      |
| nbody                      | 71.9 ms                                                     | 62.7 ms: 1.15x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.6 ms: 1.15x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.84 us: 1.14x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 59.0 ms: 1.14x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 78.8 ms: 1.11x faster                                                      |
| chaos                      | 43.3 ms                                                     | 39.1 ms: 1.11x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 40.9 ms: 1.08x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.5 ms: 1.08x faster                                                      |
| raytrace                   | 192 ms                                                      | 179 ms: 1.08x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.61 ms: 1.07x faster                                                      |
| scimark_fft                | 184 ms                                                      | 172 ms: 1.07x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 58.9 ms: 1.07x faster                                                      |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.07x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 87.9 ms: 1.06x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.53 ms: 1.06x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 74.7 ms: 1.05x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.0 ms: 1.05x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 87.4 ms: 1.05x faster                                                      |
| async_generators           | 239 ms                                                      | 229 ms: 1.04x faster                                                       |
| richards_super             | 32.1 ms                                                     | 30.7 ms: 1.04x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.04x faster                                                      |
| sympy_str                  | 175 ms                                                      | 168 ms: 1.04x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 72.0 ms: 1.04x faster                                                      |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                       |
| pyflate                    | 295 ms                                                      | 286 ms: 1.03x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 13.9 ms: 1.03x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.62 sec: 1.03x faster                                                     |
| crypto_pyaes               | 48.5 ms                                                     | 47.4 ms: 1.02x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 4.01 ms: 1.02x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 63.8 ms: 1.02x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.52 ms: 1.02x faster                                                      |
| json                       | 3.05 ms                                                     | 3.02 ms: 1.01x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.35 sec: 1.01x faster                                                     |
| unpickle_pure_python       | 133 us                                                      | 132 us: 1.01x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 2.18 ms: 1.01x slower                                                      |
| 2to3                       | 218 ms                                                      | 220 ms: 1.01x slower                                                       |
| pycparser                  | 699 ms                                                      | 709 ms: 1.02x slower                                                       |
| sympy_expand               | 284 ms                                                      | 289 ms: 1.02x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 531 ms: 1.03x slower                                                       |
| fannkuch                   | 247 ms                                                      | 256 ms: 1.04x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 39.1 ms: 1.04x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.09 sec: 1.04x slower                                                     |
| django_template            | 22.9 ms                                                     | 24.3 ms: 1.06x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 102 us: 1.07x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 214 us: 1.10x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.29 ms: 1.10x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.59 ms: 1.11x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.3 ms: 1.19x slower                                                      |
| python_startup             | 19.5 ms                                                     | 25.6 ms: 1.32x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.18 ms: 1.43x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.33 ms: 1.76x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 325 ns: 5.37x slower                                                       |
| coverage                   | 40.8 ms                                                     | 296 ms: 7.26x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (5): logging_format, regex_v8, logging_simple, scimark_lu, xml_etree_generate
Ignored benchmarks (21) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250609-3.15.0a0-b150b6a/bm-20250609-pythonperf1-amd64-python-b150b6aca7b17efe1bb1-3.15.0a0-b150b6a.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.072x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown