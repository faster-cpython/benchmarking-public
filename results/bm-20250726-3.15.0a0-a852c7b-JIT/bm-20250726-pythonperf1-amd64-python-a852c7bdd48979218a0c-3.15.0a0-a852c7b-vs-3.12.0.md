# Results vs. 3.12.0

- fork: python
- ref: a852c7bdd48979218a0c
- machine: windows-amd64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.111x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 223 ms: 1.02x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                     |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 390 ms: 1.98x faster                                                       |
| async_tree_io              | 731 ms                                                      | 394 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 213 ms: 1.72x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.66x faster                                                       |
| async_tree_none            | 291 ms                                                      | 175 ms: 1.66x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 339 ms: 1.44x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.67x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.2 ms: 1.31x faster                                                      |
| nbody          | 71.9 ms                                                     | 56.5 ms: 1.27x faster                                                      |
| pidigits       | 152 ms                                                      | 147 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 79.2 ms: 1.10x faster                                                      |
| regex_dna      | 126 ms                                                      | 121 ms: 1.04x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 106 us: 1.26x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.12 sec: 1.23x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 51.3 ms: 1.09x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.6 ms: 1.03x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 94.8 ms: 1.02x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.04x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 205 us: 1.05x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.67 us: 1.06x slower                                                      |
| pickle               | 7.43 us                                                     | 7.93 us: 1.07x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.42 ms: 1.13x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 20.8 us: 1.13x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.43 us: 1.22x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 19.7 ms: 1.22x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.2 ms: 1.35x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.42 ms: 1.31x faster                                                      |
| django_template | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 33.4 ms: 2.41x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 390 ms: 1.98x faster                                                       |
| async_tree_io              | 731 ms                                                      | 394 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 213 ms: 1.72x faster                                                       |
| mdp                        | 1.37 sec                                                    | 820 ms: 1.67x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.66x faster                                                       |
| async_tree_none            | 291 ms                                                      | 175 ms: 1.66x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 207 ms: 1.64x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.39 sec: 1.50x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 347 ms: 1.45x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 339 ms: 1.44x faster                                                       |
| deepcopy                   | 238 us                                                      | 173 us: 1.37x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.7 us: 1.32x faster                                                      |
| float                      | 56.8 ms                                                     | 43.2 ms: 1.31x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.42 ms: 1.31x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.2 us: 1.30x faster                                                      |
| nbody                      | 71.9 ms                                                     | 56.5 ms: 1.27x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 106 us: 1.26x faster                                                       |
| tomli_loads                | 1.37 sec                                                    | 1.12 sec: 1.23x faster                                                     |
| go                         | 91.6 ms                                                     | 75.1 ms: 1.22x faster                                                      |
| fannkuch                   | 247 ms                                                      | 207 ms: 1.19x faster                                                       |
| pyflate                    | 295 ms                                                      | 249 ms: 1.18x faster                                                       |
| scimark_fft                | 184 ms                                                      | 156 ms: 1.18x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 896 ms: 1.17x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 443 ms: 1.16x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.55 us: 1.13x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.88 us: 1.12x faster                                                      |
| generators                 | 22.5 ms                                                     | 20.2 ms: 1.11x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.31 ms: 1.11x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 79.2 ms: 1.10x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 34.2 ns: 1.10x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 51.3 ms: 1.09x faster                                                      |
| raytrace                   | 192 ms                                                      | 178 ms: 1.08x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.5 ms: 1.08x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 56.1 ns: 1.08x faster                                                      |
| chaos                      | 43.3 ms                                                     | 40.5 ms: 1.07x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 41.6 ms: 1.07x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 45.9 ms: 1.06x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.5 ms: 1.05x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.1 ms: 1.05x faster                                                      |
| scimark_sor                | 78.8 ms                                                     | 75.3 ms: 1.05x faster                                                      |
| regex_dna                  | 126 ms                                                      | 121 ms: 1.04x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 64.3 ms: 1.04x faster                                                      |
| pidigits                   | 152 ms                                                      | 147 ms: 1.04x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 36.6 ms: 1.03x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 72.9 ms: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 61.7 ms: 1.02x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 90.2 ms: 1.01x faster                                                      |
| hexiom                     | 4.10 ms                                                     | 4.05 ms: 1.01x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 58.4 ms: 1.01x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                     |
| coroutines                 | 14.3 ms                                                     | 14.5 ms: 1.02x slower                                                      |
| json                       | 3.05 ms                                                     | 3.11 ms: 1.02x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 94.8 ms: 1.02x slower                                                      |
| 2to3                       | 218 ms                                                      | 223 ms: 1.02x slower                                                       |
| logging_format             | 6.72 us                                                     | 6.89 us: 1.03x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.27 ms: 1.03x slower                                                      |
| async_generators           | 239 ms                                                      | 249 ms: 1.04x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.53 us: 1.04x slower                                                      |
| sympy_expand               | 284 ms                                                      | 296 ms: 1.04x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.04x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.26 ms: 1.05x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 205 us: 1.05x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.67 us: 1.06x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.93 us: 1.07x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 104 us: 1.10x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.42 ms: 1.13x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 20.8 us: 1.13x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 19.7 ms: 1.22x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.43 us: 1.22x slower                                                      |
| coverage                   | 40.8 ms                                                     | 51.1 ms: 1.25x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.2 ms: 1.35x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 95.8 ms: 1.39x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.18 ms: 1.43x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.33 ms: 1.77x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (8): pycparser, bench_thread_pool, xml_etree_iterparse, unpickle_list, regex_v8, sympy_str, sympy_integrate, asyncio_tcp
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.111x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown