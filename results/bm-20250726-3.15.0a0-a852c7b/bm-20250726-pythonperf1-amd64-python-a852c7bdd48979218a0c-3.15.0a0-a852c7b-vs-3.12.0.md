# Results vs. 3.12.0

- fork: python
- ref: a852c7bdd48979218a0c
- machine: windows-amd64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.073x faster
- HPT reliability: 99.66%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 224 ms: 1.03x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.64 sec: 1.02x faster                                                     |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 771 ms                                                      | 402 ms: 1.92x faster                                                       |
| async_tree_io              | 731 ms                                                      | 405 ms: 1.81x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                       |
| async_tree_none            | 291 ms                                                      | 177 ms: 1.65x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 174 ms: 1.64x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 214 ms: 1.58x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 335 ms: 1.46x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 349 ms: 1.44x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.64x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 43.3 ms: 1.31x faster                                                      |
| nbody          | 71.9 ms                                                     | 65.3 ms: 1.10x faster                                                      |
| pidigits       | 152 ms                                                      | 148 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.14x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 82.8 ms: 1.06x faster                                                      |
| regex_dna      | 126 ms                                                      | 122 ms: 1.04x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.6 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 90.0 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 65.2 ms                                                     | 66.4 ms: 1.02x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 140 us: 1.05x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.59 us: 1.05x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 59.1 ms: 1.06x slower                                                      |
| tomli_loads          | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                     |
| pickle_dict          | 18.4 us                                                     | 19.7 us: 1.07x slower                                                      |
| pickle               | 7.43 us                                                     | 7.94 us: 1.07x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 40.8 ms: 1.08x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.99 us: 1.09x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.24 ms: 1.10x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 219 us: 1.12x slower                                                       |
| pickle_list          | 2.83 us                                                     | 3.24 us: 1.15x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 20.1 ms: 1.23x slower                                                      |
| python_startup         | 19.5 ms                                                     | 27.0 ms: 1.39x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.31x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.82 ms: 1.04x faster                                                      |
| django_template | 22.9 ms                                                     | 25.2 ms: 1.10x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.03x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pathlib                    | 80.5 ms                                                     | 32.6 ms: 2.47x faster                                                      |
| async_tree_io_tg           | 771 ms                                                      | 402 ms: 1.92x faster                                                       |
| async_tree_io              | 731 ms                                                      | 405 ms: 1.81x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 216 ms: 1.70x faster                                                       |
| mdp                        | 1.37 sec                                                    | 816 ms: 1.68x faster                                                       |
| async_tree_none            | 291 ms                                                      | 177 ms: 1.65x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 174 ms: 1.64x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.30 sec: 1.62x faster                                                     |
| async_tree_memoization     | 339 ms                                                      | 214 ms: 1.58x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 335 ms: 1.46x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 349 ms: 1.44x faster                                                       |
| deepcopy                   | 238 us                                                      | 174 us: 1.36x faster                                                       |
| float                      | 56.8 ms                                                     | 43.3 ms: 1.31x faster                                                      |
| comprehensions             | 14.1 us                                                     | 11.0 us: 1.28x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 18.7 us: 1.27x faster                                                      |
| go                         | 91.6 ms                                                     | 77.4 ms: 1.18x faster                                                      |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.58 us: 1.11x faster                                                      |
| nbody                      | 71.9 ms                                                     | 65.3 ms: 1.10x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.90 us: 1.10x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 447 ms: 1.09x faster                                                       |
| unpack_sequence            | 37.5 ns                                                     | 34.3 ns: 1.09x faster                                                      |
| spectral_norm              | 66.9 ms                                                     | 61.6 ms: 1.09x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 40.8 ms: 1.09x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.9 ms: 1.07x faster                                                      |
| regex_compile              | 87.5 ms                                                     | 82.8 ms: 1.06x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 57.6 ns: 1.05x faster                                                      |
| async_generators           | 239 ms                                                      | 230 ms: 1.04x faster                                                       |
| regex_dna                  | 126 ms                                                      | 122 ms: 1.04x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.82 ms: 1.04x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 88.3 ms: 1.04x faster                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 90.0 ms: 1.03x faster                                                      |
| sympy_integrate            | 13.0 ms                                                     | 12.5 ms: 1.03x faster                                                      |
| meteor_contest             | 74.6 ms                                                     | 72.4 ms: 1.03x faster                                                      |
| raytrace                   | 192 ms                                                      | 187 ms: 1.03x faster                                                       |
| pidigits                   | 152 ms                                                      | 148 ms: 1.03x faster                                                       |
| chaos                      | 43.3 ms                                                     | 42.3 ms: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.58 us: 1.02x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.03 sec: 1.02x faster                                                     |
| scimark_sor                | 78.8 ms                                                     | 77.3 ms: 1.02x faster                                                      |
| richards_super             | 32.1 ms                                                     | 31.5 ms: 1.02x faster                                                      |
| docutils                   | 1.66 sec                                                    | 1.64 sec: 1.02x faster                                                     |
| logging_simple             | 6.28 us                                                     | 6.18 us: 1.01x faster                                                      |
| scimark_fft                | 184 ms                                                      | 183 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.58 ms: 1.01x slower                                                      |
| sympy_expand               | 284 ms                                                      | 287 ms: 1.01x slower                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.4 ms: 1.02x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 49.4 ms: 1.02x slower                                                      |
| json                       | 3.05 ms                                                     | 3.11 ms: 1.02x slower                                                      |
| 2to3                       | 218 ms                                                      | 224 ms: 1.03x slower                                                       |
| regex_v8                   | 14.2 ms                                                     | 14.6 ms: 1.03x slower                                                      |
| coroutines                 | 14.3 ms                                                     | 14.7 ms: 1.03x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.23 ms: 1.03x slower                                                      |
| pycparser                  | 699 ms                                                      | 723 ms: 1.04x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 65.2 ms: 1.04x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 140 us: 1.05x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.59 us: 1.05x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 59.1 ms: 1.06x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                     |
| deltablue                  | 2.16 ms                                                     | 2.29 ms: 1.06x slower                                                      |
| pickle_dict                | 18.4 us                                                     | 19.7 us: 1.07x slower                                                      |
| pickle                     | 7.43 us                                                     | 7.94 us: 1.07x slower                                                      |
| fannkuch                   | 247 ms                                                      | 264 ms: 1.07x slower                                                       |
| xml_etree_process          | 37.7 ms                                                     | 40.8 ms: 1.08x slower                                                      |
| unpickle_list              | 2.75 us                                                     | 2.99 us: 1.09x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.24 ms: 1.10x slower                                                      |
| django_template            | 22.9 ms                                                     | 25.2 ms: 1.10x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 105 us: 1.10x slower                                                       |
| pickle_pure_python         | 195 us                                                      | 219 us: 1.12x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.69 ms: 1.13x slower                                                      |
| pickle_list                | 2.83 us                                                     | 3.24 us: 1.15x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 20.1 ms: 1.23x slower                                                      |
| coverage                   | 40.8 ms                                                     | 51.9 ms: 1.27x slower                                                      |
| python_startup             | 19.5 ms                                                     | 27.0 ms: 1.39x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 2.11 ms: 1.39x slower                                                      |
| bench_mp_pool              | 69.2 ms                                                     | 96.6 ms: 1.40x slower                                                      |
| create_gc_cycles           | 752 us                                                      | 1.30 ms: 1.73x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.06x faster                                                               |

Benchmark hidden because not significant (6): sympy_str, scimark_lu, pyflate, pprint_safe_repr, bench_thread_pool, richards
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (17) of results/bm-20250726-3.15.0a0-a852c7b/bm-20250726-pythonperf1-amd64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: asyncio_websockets, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.073x faster

# HPT report

- Reliability score: 99.66% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown