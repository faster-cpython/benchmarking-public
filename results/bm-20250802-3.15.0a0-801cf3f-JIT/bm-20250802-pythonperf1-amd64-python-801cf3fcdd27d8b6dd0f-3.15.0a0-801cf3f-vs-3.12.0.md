# Results vs. 3.12.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: windows-amd64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.116x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 224 ms: 1.03x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                     |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 392 ms: 1.97x faster                                                       |
| async_tree_io              | 731 ms                                                      | 394 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 214 ms: 1.72x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.66x faster                                                       |
| async_tree_none            | 291 ms                                                      | 180 ms: 1.61x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 211 ms: 1.61x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 335 ms: 1.46x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 349 ms: 1.44x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.66x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 44.7 ms: 1.27x faster                                                      |
| nbody          | 71.9 ms                                                     | 60.5 ms: 1.19x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 77.9 ms: 1.12x faster                                                      |
| regex_dna      | 126 ms                                                      | 116 ms: 1.09x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.5 ms: 1.05x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 133 us                                                      | 105 us: 1.27x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.10 sec: 1.24x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 50.3 ms: 1.11x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 86.7 ms: 1.07x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 35.5 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.5 ms: 1.04x faster                                                      |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| pickle               | 7.43 us                                                     | 7.84 us: 1.05x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.91 us: 1.06x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 209 us: 1.07x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.79 us: 1.07x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.13 ms: 1.08x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 20.6 us: 1.12x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.35 us: 1.18x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.0 ms: 1.23x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.6 ms: 1.37x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.35 ms: 1.33x faster                                                      |
| django_template | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.5 ms: 2.47x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 392 ms: 1.97x faster                                                       |
| async_tree_io              | 731 ms                                                      | 394 ms: 1.85x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 214 ms: 1.72x faster                                                       |
| mdp                        | 1.37 sec                                                    | 819 ms: 1.67x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 171 ms: 1.66x faster                                                       |
| async_tree_none            | 291 ms                                                      | 180 ms: 1.61x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 211 ms: 1.61x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.41 sec: 1.48x faster                                                     |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 335 ms: 1.46x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 349 ms: 1.44x faster                                                       |
| deepcopy                   | 238 us                                                      | 169 us: 1.41x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 17.8 us: 1.33x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.35 ms: 1.33x faster                                                      |
| comprehensions             | 14.1 us                                                     | 10.8 us: 1.31x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 105 us: 1.27x faster                                                       |
| float                      | 56.8 ms                                                     | 44.7 ms: 1.27x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.10 sec: 1.24x faster                                                     |
| scimark_fft                | 184 ms                                                      | 149 ms: 1.24x faster                                                       |
| go                         | 91.6 ms                                                     | 77.0 ms: 1.19x faster                                                      |
| nbody                      | 71.9 ms                                                     | 60.5 ms: 1.19x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.80 us: 1.16x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.8 ms: 1.14x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.25 ms: 1.14x faster                                                      |
| pprint_safe_repr           | 513 ms                                                      | 454 ms: 1.13x faster                                                       |
| pprint_pformat             | 1.05 sec                                                    | 930 ms: 1.12x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 77.9 ms: 1.12x faster                                                      |
| fannkuch                   | 247 ms                                                      | 220 ms: 1.12x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 50.3 ms: 1.11x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 54.9 ns: 1.10x faster                                                      |
| regex_dna                  | 126 ms                                                      | 116 ms: 1.09x faster                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.2 ms: 1.09x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 86.7 ms: 1.07x faster                                                      |
| pyflate                    | 295 ms                                                      | 275 ms: 1.07x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 41.3 ms: 1.07x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 35.5 ms: 1.06x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 45.8 ms: 1.06x faster                                                      |
| raytrace                   | 192 ms                                                      | 182 ms: 1.06x faster                                                       |
| regex_v8                   | 14.2 ms                                                     | 13.5 ms: 1.05x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 71.0 ms: 1.05x faster                                                      |
| richards                   | 28.4 ms                                                     | 27.0 ms: 1.05x faster                                                      |
| richards_super             | 32.1 ms                                                     | 30.6 ms: 1.05x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 35.8 ns: 1.05x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.55 ms: 1.05x faster                                                      |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.5 ms: 1.04x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 88.2 ms: 1.04x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.48 us: 1.04x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.07 us: 1.03x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 61.0 ms: 1.03x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 65.4 ms: 1.02x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.7 ms: 1.02x faster                                                      |
| sympy_str                  | 175 ms                                                      | 172 ms: 1.02x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 77.3 ms: 1.02x faster                                                      |
| scimark_lu                 | 58.9 ms                                                     | 57.9 ms: 1.02x faster                                                      |
| chaos                      | 43.3 ms                                                     | 42.7 ms: 1.01x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.65 sec: 1.01x faster                                                     |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.01x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.17 ms: 1.02x slower                                                      |
| json                       | 3.05 ms                                                     | 3.11 ms: 1.02x slower                                                      |
| 2to3                       | 218 ms                                                      | 224 ms: 1.03x slower                                                       |
| async_generators           | 239 ms                                                      | 247 ms: 1.03x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.27 ms: 1.03x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.8 ms: 1.04x slower                                                      |
| sympy_expand               | 284 ms                                                      | 299 ms: 1.05x slower                                                       |
| pickle                     | 7.43 us                                                     | 7.84 us: 1.05x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.91 us: 1.06x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 209 us: 1.07x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.79 us: 1.07x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.13 ms: 1.08x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 527 ms: 1.08x slower                                                       |
| django_template            | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 106 us: 1.11x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 20.6 us: 1.12x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.35 us: 1.18x slower                                                      |
| coverage                   | 40.8 ms                                                     | 48.5 ms: 1.19x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 20.0 ms: 1.23x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.6 ms: 1.37x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 95.6 ms: 1.38x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.14 ms: 1.41x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.30 ms: 1.73x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.09x faster                                                               |

Benchmark hidden because not significant (4): pidigits, pycparser, bench_thread_pool, deltablue
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.116x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown