# Results vs. 3.12.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: windows-amd64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.022x slower
- HPT reliability: 98.81%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 232 ms: 1.07x slower                                                       |
| docutils       | 1.66 sec                                                    | 2.97 sec: 1.79x slower                                                     |
| Geometric mean | (ref)                                                       | 1.38x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 335 ms: 2.30x faster                                                       |
| async_tree_io              | 731 ms                                                      | 352 ms: 2.07x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 155 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 203 ms: 1.81x faster                                                       |
| async_tree_none            | 291 ms                                                      | 178 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 316 ms: 1.59x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.52x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 345 ms: 1.42x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.75x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 46.4 ms: 1.22x faster                                                      |
| pidigits       | 152 ms                                                      | 142 ms: 1.07x faster                                                       |
| nbody          | 71.9 ms                                                     | 82.2 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 112 ms: 1.12x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 13.1 ms: 1.08x faster                                                      |
| regex_effbot   | 1.62 ms                                                     | 1.51 ms: 1.07x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 94.4 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                       | 1.05x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_iterparse  | 65.2 ms                                                     | 59.5 ms: 1.09x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 90.6 ms: 1.03x faster                                                      |
| unpickle_list        | 2.75 us                                                     | 3.10 us: 1.13x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 63.1 ms: 1.13x slower                                                      |
| json_loads           | 13.9 us                                                     | 15.8 us: 1.14x slower                                                      |
| pickle               | 7.43 us                                                     | 8.47 us: 1.14x slower                                                      |
| pickle_list          | 2.83 us                                                     | 3.23 us: 1.14x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 21.2 us: 1.15x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 44.2 ms: 1.17x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 157 us: 1.18x slower                                                       |
| json_dumps           | 5.70 ms                                                     | 6.72 ms: 1.18x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 242 us: 1.24x slower                                                       |
| unpickle             | 8.18 us                                                     | 10.6 us: 1.30x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 2.77 sec: 2.03x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.18x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.2 ms: 1.24x slower                                                      |
| python_startup         | 19.5 ms                                                     | 27.0 ms: 1.39x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 27.3 ms: 1.19x slower                                                      |
| mako            | 7.09 ms                                                     | 9.71 ms: 1.37x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.28x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.7 ms: 2.46x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 335 ms: 2.30x faster                                                       |
| async_tree_io              | 731 ms                                                      | 352 ms: 2.07x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 155 ms: 1.84x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 203 ms: 1.81x faster                                                       |
| async_tree_none            | 291 ms                                                      | 178 ms: 1.64x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 316 ms: 1.59x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 224 ms: 1.52x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 345 ms: 1.42x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.36 us: 1.30x faster                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.22 ms: 1.25x faster                                                      |
| float                      | 56.8 ms                                                     | 46.4 ms: 1.22x faster                                                      |
| deepcopy                   | 238 us                                                      | 203 us: 1.17x faster                                                       |
| mdp                        | 1.37 sec                                                    | 1.18 sec: 1.16x faster                                                     |
| deepcopy_memo              | 23.7 us                                                     | 20.9 us: 1.13x faster                                                      |
| comprehensions             | 14.1 us                                                     | 12.5 us: 1.13x faster                                                      |
| regex_dna                  | 126 ms                                                      | 112 ms: 1.12x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 59.5 ms: 1.09x faster                                                      |
| regex_v8                   | 14.2 ms                                                     | 13.1 ms: 1.08x faster                                                      |
| pidigits                   | 152 ms                                                      | 142 ms: 1.07x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.51 ms: 1.07x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 42.9 ms: 1.03x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 90.6 ms: 1.03x faster                                                      |
| go                         | 91.6 ms                                                     | 92.9 ms: 1.01x slower                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 2.13 us: 1.02x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 62.1 ns: 1.03x slower                                                      |
| generators                 | 22.5 ms                                                     | 23.2 ms: 1.03x slower                                                      |
| json                       | 3.05 ms                                                     | 3.15 ms: 1.03x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 39.1 ns: 1.04x slower                                                      |
| pycparser                  | 699 ms                                                      | 731 ms: 1.05x slower                                                       |
| coroutines                 | 14.3 ms                                                     | 15.1 ms: 1.06x slower                                                      |
| 2to3                       | 218 ms                                                      | 232 ms: 1.07x slower                                                       |
| logging_simple             | 6.28 us                                                     | 6.72 us: 1.07x slower                                                      |
| logging_format             | 6.72 us                                                     | 7.23 us: 1.08x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 94.4 ms: 1.08x slower                                                      |
| chaos                      | 43.3 ms                                                     | 46.9 ms: 1.08x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 14.2 ms: 1.10x slower                                                      |
| raytrace                   | 192 ms                                                      | 211 ms: 1.10x slower                                                       |
| async_generators           | 239 ms                                                      | 263 ms: 1.10x slower                                                       |
| sympy_str                  | 175 ms                                                      | 193 ms: 1.10x slower                                                       |
| pprint_safe_repr           | 513 ms                                                      | 567 ms: 1.11x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 74.2 ms: 1.11x slower                                                      |
| pyflate                    | 295 ms                                                      | 328 ms: 1.11x slower                                                       |
| sympy_sum                  | 91.5 ms                                                     | 102 ms: 1.12x slower                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 2.34 sec: 1.12x slower                                                     |
| unpickle_list              | 2.75 us                                                     | 3.10 us: 1.13x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 63.1 ms: 1.13x slower                                                      |
| sympy_expand               | 284 ms                                                      | 322 ms: 1.14x slower                                                       |
| json_loads                 | 13.9 us                                                     | 15.8 us: 1.14x slower                                                      |
| pickle                     | 7.43 us                                                     | 8.47 us: 1.14x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.67 ms: 1.14x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 89.8 ms: 1.14x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.23 us: 1.14x slower                                                      |
| nbody                      | 71.9 ms                                                     | 82.2 ms: 1.14x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.48 ms: 1.15x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 21.2 us: 1.15x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 68.2 ms: 1.16x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 80.7 ms: 1.17x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 56.8 ms: 1.17x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 44.2 ms: 1.17x slower                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 51.5 ms: 1.18x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 157 us: 1.18x slower                                                       |
| json_dumps                 | 5.70 ms                                                     | 6.72 ms: 1.18x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 74.6 ms: 1.19x slower                                                      |
| django_template            | 22.9 ms                                                     | 27.3 ms: 1.19x slower                                                      |
| fannkuch                   | 247 ms                                                      | 294 ms: 1.19x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 89.1 ms: 1.19x slower                                                      |
| scimark_fft                | 184 ms                                                      | 227 ms: 1.23x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 242 us: 1.24x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 20.2 ms: 1.24x slower                                                      |
| richards                   | 28.4 ms                                                     | 35.5 ms: 1.25x slower                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 3.20 ms: 1.25x slower                                                      |
| bench_thread_pool          | 857 us                                                      | 1.10 ms: 1.28x slower                                                      |
| richards_super             | 32.1 ms                                                     | 41.3 ms: 1.29x slower                                                      |
| telco                      | 4.13 ms                                                     | 5.34 ms: 1.29x slower                                                      |
| unpickle                   | 8.18 us                                                     | 10.6 us: 1.30x slower                                                      |
| mako                       | 7.09 ms                                                     | 9.71 ms: 1.37x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 130 us: 1.37x slower                                                       |
| python_startup             | 19.5 ms                                                     | 27.0 ms: 1.39x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.05 ms: 1.39x slower                                                      |
| coverage                   | 40.8 ms                                                     | 66.3 ms: 1.62x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.72 sec: 1.65x slower                                                     |
| docutils                   | 1.66 sec                                                    | 2.97 sec: 1.79x slower                                                     |
| tomli_loads                | 1.37 sec                                                    | 2.77 sec: 2.03x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): asyncio_tcp
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-pythonperf1-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.022x slower

# HPT report

- Reliability score: 98.81% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown