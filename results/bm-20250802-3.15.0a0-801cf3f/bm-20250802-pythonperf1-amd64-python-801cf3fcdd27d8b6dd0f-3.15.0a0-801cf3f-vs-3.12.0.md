# Results vs. 3.12.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: windows-amd64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.063x faster
- HPT reliability: 98.57%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 225 ms: 1.03x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                     |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 406 ms: 1.90x faster                                                       |
| async_tree_io              | 731 ms                                                      | 405 ms: 1.80x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 219 ms: 1.68x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 173 ms: 1.65x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 215 ms: 1.58x faster                                                       |
| async_tree_none            | 291 ms                                                      | 188 ms: 1.55x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 356 ms: 1.41x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 347 ms: 1.41x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.61x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.2 ms: 1.23x faster                                                      |
| nbody          | 71.9 ms                                                     | 67.0 ms: 1.07x faster                                                      |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 81.2 ms: 1.08x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.52 ms: 1.06x faster                                                      |
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.9 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                       | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 68.0 ms: 1.04x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 58.6 ms: 1.05x slower                                                      |
| unpickle             | 8.18 us                                                     | 8.67 us: 1.06x slower                                                      |
| pickle               | 7.43 us                                                     | 7.90 us: 1.06x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 40.7 ms: 1.08x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 144 us: 1.08x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.21 ms: 1.09x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 20.2 us: 1.09x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 3.03 us: 1.10x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 223 us: 1.14x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.28 us: 1.16x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.3 ms: 1.25x slower                                                      |
| python_startup         | 19.5 ms                                                     | 26.9 ms: 1.38x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.67 ms: 1.06x faster                                                      |
| django_template | 22.9 ms                                                     | 24.6 ms: 1.07x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.00x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.5 ms: 2.47x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 406 ms: 1.90x faster                                                       |
| async_tree_io              | 731 ms                                                      | 405 ms: 1.80x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 219 ms: 1.68x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 173 ms: 1.65x faster                                                       |
| mdp                        | 1.37 sec                                                    | 834 ms: 1.65x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 215 ms: 1.58x faster                                                       |
| async_tree_none            | 291 ms                                                      | 188 ms: 1.55x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.42 sec: 1.47x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 356 ms: 1.41x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 347 ms: 1.41x faster                                                       |
| deepcopy                   | 238 us                                                      | 172 us: 1.38x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 18.1 us: 1.31x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.2 us: 1.27x faster                                                      |
| float                      | 56.8 ms                                                     | 46.2 ms: 1.23x faster                                                      |
| go                         | 91.6 ms                                                     | 80.7 ms: 1.13x faster                                                      |
| generators                 | 22.5 ms                                                     | 20.0 ms: 1.13x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.87 us: 1.12x faster                                                      |
| unpack_sequence            | 37.5 ns                                                     | 33.7 ns: 1.11x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.59 us: 1.11x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 81.2 ms: 1.08x faster                                                      |
| raytrace                   | 192 ms                                                      | 179 ms: 1.08x faster                                                       |
| nbody                      | 71.9 ms                                                     | 67.0 ms: 1.07x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 56.6 ns: 1.07x faster                                                      |
| mako                       | 7.09 ms                                                     | 6.67 ms: 1.06x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.52 ms: 1.06x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 41.2 ms: 1.06x faster                                                      |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                       |
| chaos                      | 43.3 ms                                                     | 42.0 ms: 1.03x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 88.9 ms: 1.03x faster                                                      |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                       |
| sympy_str                  | 175 ms                                                      | 171 ms: 1.03x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.6 ms: 1.03x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.9 ms: 1.03x faster                                                      |
| logging_simple             | 6.28 us                                                     | 6.17 us: 1.02x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 65.9 ms: 1.02x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.62 us: 1.02x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                     |
| pprint_safe_repr           | 513 ms                                                      | 507 ms: 1.01x faster                                                       |
| json                       | 3.05 ms                                                     | 3.07 ms: 1.01x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 48.9 ms: 1.01x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.4 ms: 1.01x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 63.7 ms: 1.01x slower                                                      |
| pyflate                    | 295 ms                                                      | 302 ms: 1.03x slower                                                       |
| deltablue                  | 2.16 ms                                                     | 2.22 ms: 1.03x slower                                                      |
| richards_super             | 32.1 ms                                                     | 33.0 ms: 1.03x slower                                                      |
| 2to3                       | 218 ms                                                      | 225 ms: 1.03x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.03x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.25 ms: 1.04x slower                                                      |
| scimark_fft                | 184 ms                                                      | 191 ms: 1.04x slower                                                       |
| asyncio_tcp                | 487 ms                                                      | 507 ms: 1.04x slower                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 68.0 ms: 1.04x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.43 sec: 1.05x slower                                                     |
| pycparser                  | 699 ms                                                      | 732 ms: 1.05x slower                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.68 ms: 1.05x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 58.6 ms: 1.05x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 62.2 ms: 1.06x slower                                                      |
| sympy_expand               | 284 ms                                                      | 300 ms: 1.06x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.67 us: 1.06x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.90 us: 1.06x slower                                                      |
| django_template            | 22.9 ms                                                     | 24.6 ms: 1.07x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 40.7 ms: 1.08x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 144 us: 1.08x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.21 ms: 1.09x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 20.2 us: 1.09x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 3.03 us: 1.10x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.11x slower                                                       |
| fannkuch                   | 247 ms                                                      | 277 ms: 1.12x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.64 ms: 1.12x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 223 us: 1.14x slower                                                       |
| pickle_list                | 2.83 us                                                     | 3.28 us: 1.16x slower                                                      |
| coverage                   | 40.8 ms                                                     | 49.9 ms: 1.22x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 20.3 ms: 1.25x slower                                                      |
| python_startup             | 19.5 ms                                                     | 26.9 ms: 1.38x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 96.1 ms: 1.39x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.17 ms: 1.42x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.39 ms: 1.85x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.05x faster                                                               |

Benchmark hidden because not significant (8): xml_etree_parse, dulwich_log, async_generators, meteor_contest, pprint_pformat, scimark_sor, richards, bench_thread_pool
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 98.57% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown